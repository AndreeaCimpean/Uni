#include "service.h"
#include "repository.h"
#include "ui.h"

int main()
{
	Repository repository = create_repository();
	Service service = create_service(&repository);
	UI ui = create_ui(&service);
	start(&ui);
	return 0;
}
