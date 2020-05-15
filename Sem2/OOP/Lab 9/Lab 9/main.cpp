#include <crtdbg.h>
#include "MemoryRepository.h"
#include "EvidenceValidator.h"
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
		EvidenceValidator evidenceValidator;
		TextFileRepository physicalCopiesRepository{};
		Service service{ evidenceValidator, repository, physicalCopiesRepository };
		UI ui{ service };
		ui.run();
	}
	_CrtDumpMemoryLeaks();
	return 0;
}