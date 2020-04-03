#include <crtdbg.h>
#include "Repository.h"
#include "Service.h"
#include "UI.h"
#include "Repository.h"
#include "tests.h"

using namespace std;

int main()
{
	test_all();
	{
		Repository repository{};
		Service service{ repository };
		UI ui{ service };
		ui.run();
	}
	_CrtDumpMemoryLeaks();
	return 0;
}