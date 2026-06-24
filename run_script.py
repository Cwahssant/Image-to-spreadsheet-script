import sys
import install_missing_libraries

if len(sys.argv) < 2:
    print("Please provide image file")
    sys.exit(1)

install_missing_libraries.check_dependencies()

import Image_to_data

Image_to_data.main(sys.argv[1])