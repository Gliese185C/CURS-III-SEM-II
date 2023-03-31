#ifndef INCLUDED_DA_7Z_H
#define INCLUDED_DA_7Z_H

#include "da-library.h"
#include <7zip/C/7z.h>
#include <7zip/C/Types.h>

namespace da {
	
	class DA7ZIP_API DA_7Z {
		
		public:
			
			DA_7Z(ILookInStream* stream);
			
			bool is_open();
			
			bool is_dir(size_t i);

			UInt64 get_filename_length_UTF16(size_t i);

			bool get_filename_UTF16(size_t i, char* name);

			UInt64 get_filesize(size_t i);

			UInt64 get_compression_method(size_t fileIndex, size_t coderIndex);

			/// Function gives the unpacked size of the file
			UInt64 get_unpacksize(size_t fileIndex);

			/// Function gives the unpacked size of the streams of the different streams within a file
			UInt64 get_unpacksizeofstream(size_t fileIndex, size_t coderIndex);

			UInt64 get_fileoffset(size_t i);

			UInt64 get_streamoffset(size_t i);

			UInt64 get_streamsize(size_t i);

			UInt64 get_packsizes(size_t fileIndex, size_t si);

			UInt64 get_file_modifiedtime(size_t i);

			UInt64 get_total_file_count();

			UInt64 get_total_folder_count();

			UInt64 get_total_coders(size_t fileIndex);
			
			unsigned char* get_Props_data(size_t fileIndex, size_t coderIndex);

			UInt64 get_Props_size(size_t fileIndex, size_t coderIndex);

			UInt64 get_CRC(size_t fileIndex);

			bool is_folder_supported(size_t fileIndex);

		private:
			CSzArEx _db;
			bool _fail;
	};
}
#endif