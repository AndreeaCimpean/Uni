#define _CRTDBG_MAP_ALLOC
#include "service.h"
#include "repository.h"
#include "ui.h"
#include "operationStack.h"
#include <stdlib.h>
#include <crtdbg.h>
#include "tests.h"

int main()
{
	test_all();
	Repository* repository = create_repository();
	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Service* service = create_service(repository, undoStack, redoStack);
	UI* ui = create_ui(service);
	start(ui);
	destroy_ui(ui);

	_CrtDumpMemoryLeaks();
	return 0;
}
