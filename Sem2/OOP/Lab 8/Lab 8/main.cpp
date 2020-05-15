#include <crtdbg.h>
#include "MemoryRepository.h"
#include "TextFileRepository.h"
#include "Service.h"
#include "UI.h"
#include "tests.h"

using namespace std;

int main()
{
	//test_all();
	{
		//MemoryRepository repository{};
		TextFileRepository repository{};
		Service service{ repository };
		UI ui{ service };
		ui.run();
	}
	_CrtDumpMemoryLeaks();
	return 0;
}