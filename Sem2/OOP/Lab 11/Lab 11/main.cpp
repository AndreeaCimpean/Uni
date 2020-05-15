#include "Lab11.h"
#include <QtWidgets/QApplication>
#include "MemoryRepository.h"
#include "EvidenceValidator.h"
#include "TextFileRepository.h"
#include "CSVRepository.h"
#include "HTMLRepository.h"
#include "Service.h"
#include "qmessagebox.h"
#include "GUI.h"

int main(int argc, char* argv[])
{
	QApplication application(argc, argv);
	TextFileRepository repository{};
	EvidenceValidator evidenceValidator;
	TextFileRepository physicalCopiesRepository{};
	Service service{ evidenceValidator, repository, physicalCopiesRepository };
	GUI gui{ service };
	gui.selectFiles->show();
	return application.exec();
}
