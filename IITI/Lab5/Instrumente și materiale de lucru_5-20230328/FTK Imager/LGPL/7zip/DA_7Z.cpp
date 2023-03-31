#include "DA_7Z.h"
#include <cstdio>
#include <iostream>
#include <7zip/C/7z.h>
#include <7zip/C/7zCrc.h>
extern "C" {
#include <7zip/C/7zAlloc.h>
}

#define SEVENZIP_Copy 0
#define SEVENZIP_LZMA2 0x21
#define SEVENZIP_LZMA  0x30101
#define SEVENZIP_BZIP2 0x40202
#define SEVENZIP_Deflate 0x40108
#define SEVENZIP_BCJ   0x03030103
#define SEVENZIP_BCJ2  0x0303011B

#ifdef _7ZIP_PPMD_SUPPPORT
#define SEVENZIP_PPMD 0x30401
#endif

namespace da{

	static bool IS_MAIN_METHOD(UInt32 m)
	{
		switch(m)
		{
		case SEVENZIP_Copy:
		case SEVENZIP_LZMA:
		case SEVENZIP_LZMA2:
		case SEVENZIP_BZIP2:
		case SEVENZIP_Deflate:
#ifdef _7ZIP_PPMD_SUPPPORT
		case SEVENZIP_PPMD:
#endif
			return true;
		}
		return false;
	}

	static Bool IS_SUPPORTED_CODER(const CSzCoderInfo *c)
	{
		return
			c->NumInStreams == 1 &&
			c->NumOutStreams == 1 &&
			c->MethodID <= (UInt32)0xFFFFFFFF &&
			IS_MAIN_METHOD((UInt32)c->MethodID);
	}

	inline bool IS_BCJ2(CSzCoderInfo* c) { return ((c)->MethodID == SEVENZIP_BCJ2 && (c)->NumInStreams == 4 && (c)->NumOutStreams == 1);}

	static SRes CheckSupportedFolder(const CSzFolder *f)
	{
		if (f->NumCoders < 1 || f->NumCoders > 4)
			return SZ_ERROR_UNSUPPORTED;
		if (!IS_SUPPORTED_CODER(&f->Coders[0]))
			return SZ_ERROR_UNSUPPORTED;
		if (f->NumCoders == 1)
		{
			if (f->NumPackStreams != 1 || f->PackStreams[0] != 0 || f->NumBindPairs != 0)
				return SZ_ERROR_UNSUPPORTED;
			return SZ_OK;
		}
		if (f->NumCoders == 2)
		{
			CSzCoderInfo *c = &f->Coders[1];
			if (c->MethodID > (UInt32)0xFFFFFFFF ||
				c->NumInStreams != 1 ||
				c->NumOutStreams != 1 ||
				f->NumPackStreams != 1 ||
				f->PackStreams[0] != 0 ||
				f->NumBindPairs != 1 ||
				f->BindPairs[0].InIndex != 1 ||
				f->BindPairs[0].OutIndex != 0)
				return SZ_ERROR_UNSUPPORTED;
			switch ((UInt32)c->MethodID)
			{
			case SEVENZIP_BCJ:
				/*case SEVENZIP_ARM:*/
				break;
			default:
				return SZ_ERROR_UNSUPPORTED;
			}
			return SZ_OK;
		}
		if (f->NumCoders == 4)
		{
			if (!IS_SUPPORTED_CODER(&f->Coders[1]) ||
				!IS_SUPPORTED_CODER(&f->Coders[2]) ||
				!IS_BCJ2(&f->Coders[3]))
				return SZ_ERROR_UNSUPPORTED;
			if (f->NumPackStreams != 4 ||
				f->PackStreams[0] != 2 ||
				f->PackStreams[1] != 6 ||
				f->PackStreams[2] != 1 ||
				f->PackStreams[3] != 0 ||
				f->NumBindPairs != 3 ||
				f->BindPairs[0].InIndex != 5 || f->BindPairs[0].OutIndex != 0 ||
				f->BindPairs[1].InIndex != 4 || f->BindPairs[1].OutIndex != 1 ||
				f->BindPairs[2].InIndex != 3 || f->BindPairs[2].OutIndex != 2)
				return SZ_ERROR_UNSUPPORTED;
			return SZ_OK;
		}
		return SZ_ERROR_UNSUPPORTED;
	}


	DA_7Z::DA_7Z(ILookInStream* is):_fail(false){
		ISzAlloc temp;
		ISzAlloc temp2;
		temp.Alloc = SzAlloc;
		temp.Free = SzFree;

		temp2.Alloc = SzAllocTemp;
		temp2.Free = SzFreeTemp;

		CrcGenerateTable();

		 SzArEx_Init(&_db);
		if(SzArEx_Open(&_db, is, &temp, &temp2) != SZ_OK)
			_fail = true;
	}

	bool DA_7Z::is_open(){
		return !(_fail);
	}

	bool DA_7Z::is_dir(size_t i){
		const CSzFileItem *f = _db.db.Files + i;
		
		if(f->IsDir)
			return true;

		return false;
	}

	UInt64 DA_7Z::get_filename_length_UTF16(size_t i){
		return SzArEx_GetFileNameUtf16(&_db, i, NULL);
	}

	bool DA_7Z::get_filename_UTF16(size_t i, char* name){
		if(name == NULL)
			return false;

		SzArEx_GetFileNameUtf16(&_db, i, (UInt16*)name);
		return true;
	}

	UInt64 DA_7Z::get_filesize(size_t i){
		const CSzFileItem *f = _db.db.Files + i;
		return f->Size;
	}

	UInt64 DA_7Z::get_compression_method(size_t fileIndex, size_t coderIndex){
		//const CSzFileItem *f = _db.db.Files + i;
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		CSzFolder *folder = _db.db.Folders + folderIndex;

		return folder->Coders[coderIndex].MethodID;
		//return 0;
	}

	UInt64 DA_7Z::get_unpacksize(size_t fileIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		if (folderIndex == (UInt32)-1)
			return 0;

		CSzFolder *folder = _db.db.Folders + folderIndex;
		return SzFolder_GetUnpackSize(folder);
	}

	UInt64 DA_7Z::get_unpacksizeofstream(size_t fileIndex, size_t coderIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		CSzFolder *folder = _db.db.Folders + folderIndex;

		return folder->UnpackSizes[coderIndex];
	}

	UInt64 DA_7Z::get_fileoffset(size_t fileIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		 CSzFileItem *fileItem = _db.db.Files + fileIndex;
		size_t offset(0);
		for (unsigned int i(_db.FolderStartFileIndex[folderIndex]); i < fileIndex; ++i)
		  offset += (UInt32)(_db.db.Files[i].Size);
		
		return offset;
	}

	UInt64 DA_7Z::get_streamoffset(size_t fileIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		return SzArEx_GetFolderStreamPos(&_db, folderIndex, 0);
	}

	UInt64 DA_7Z::get_streamsize(size_t fileIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		return (*(_db.db.PackSizes + _db.FolderStartPackStreamIndex[folderIndex]));
	}
	
	UInt64 DA_7Z::get_packsizes(size_t fileIndex, size_t si)
	{
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		CSzFolder *folder = _db.db.Folders + folderIndex;
		
		return (_db.db.PackSizes + _db.FolderStartPackStreamIndex[folderIndex])[si];
	}

	UInt64 DA_7Z::get_file_modifiedtime(size_t i){
		const CSzFileItem *f = _db.db.Files + i;
		if (f->MTimeDefined)
			return (f->MTime.Low | ((UInt64)f->MTime.High << 32)) / 10000000;
		return 0;
	}

	UInt64 DA_7Z::get_total_file_count(){
		return _db.db.NumFiles;
	}
	
	UInt64 DA_7Z::get_total_folder_count(){
		return _db.db.NumFolders;
	}

	unsigned char* DA_7Z::get_Props_data(size_t fileIndex, size_t coderIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return NULL;
		CSzFolder *folder = _db.db.Folders + folderIndex;

		return (unsigned char*)folder->Coders[coderIndex].Props.data;
	}

	UInt64 DA_7Z::get_Props_size(size_t fileIndex, size_t coderIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		CSzFolder *folder = _db.db.Folders + folderIndex;

		return folder->Coders[coderIndex].Props.size;
	}

	UInt64 DA_7Z::get_CRC(size_t fileIndex){
		const CSzFileItem *f = _db.db.Files + fileIndex;
		if(f->CrcDefined)
			return f->Crc;
		return 0;
	}

	UInt64 DA_7Z::get_total_coders(size_t fileIndex){
		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return 0;

		CSzFolder *folder = _db.db.Folders + folderIndex;

		return folder->NumCoders;
	}

	bool DA_7Z::is_folder_supported(size_t fileIndex){

		UInt32 folderIndex = _db.FileIndexToFolderIndexMap[fileIndex];
		
		if (folderIndex == (UInt32)-1)
			return false;

		CSzFolder *folder = _db.db.Folders + folderIndex;
		
		if(CheckSupportedFolder(folder) != SZ_OK)
			return false;

		return true;
	}
}
