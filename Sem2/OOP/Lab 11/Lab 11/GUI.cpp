#include "GUI.h"
#include <qmessagebox.h>
#include <string>
#include "CSVRepository.h"
#include "HTMLRepository.h"

using namespace std;

GUI::GUI(Service& service) : service{service}
{
	this->select_files_window();
	this->init_gui();
	this->connect_signal_and_slots();
}

void GUI::populate_evidences_list()
{
	this->evidencesList->clear();
	vector<Evidence> evidences = this->service.get_evidences();
	for (auto evidence : evidences)
		this->evidencesList->addItem(QString::fromStdString(evidence.toString()));
}

void GUI::connect_signal_and_slots()
{
	QObject::connect(this->evidencesList, &QListWidget::itemSelectionChanged, [this]() {
		int selectedIndex = this->get_selected_index();
		if (selectedIndex < 0)
			return;
		Evidence evidence = this->service.get_evidences()[selectedIndex];
		this->idLineEdit->setText(QString::fromStdString(evidence.get_id()));
		this->measurementsLineEdit->setText(QString::fromStdString(evidence.get_measurement()));
		this->photographLineEdit->setText(QString::fromStdString(evidence.get_photograph()));
		this->imageClarityLevelSpinner->setValue(evidence.get_image_clarity_level());
		this->quantitySpinner->setValue(evidence.get_quantity());

	});

	QObject::connect(this->addEvidenceButton, &QPushButton::clicked, this, &GUI::add_evidence);
	QObject::connect(this->deleteEvidenceButton, &QPushButton::clicked, this, &GUI::delete_evidence);
	QObject::connect(this->updateEvidenceButton, &QPushButton::clicked, this, &GUI::update_evidence);
	QObject::connect(this->filterEvidencesButton, &QPushButton::clicked, this, &GUI::filter_evidences);
	QObject::connect(this, &QTabWidget::currentChanged, this, [this] {
		if (this->currentIndex() == 1)
			this->set_chart();
	});
}

int GUI::get_selected_index() const
{
	QModelIndexList selectedIndexes = this->evidencesList->selectionModel()->selectedIndexes();
	if (selectedIndexes.size() == 0)
	{
		this->idLineEdit->clear();
		this->measurementsLineEdit->clear();
		this->imageClarityLevelSpinner->clear();
		this->quantitySpinner->clear();
		this->photographLineEdit->clear();
		return -1;
	}
	int selectedIndex = selectedIndexes.at(0).row();
	return selectedIndex;
}

void GUI::add_evidence()
{
	string id = this->idLineEdit->text().toStdString();
	string measurement = this->measurementsLineEdit->text().toStdString();
	string photograph = this->photographLineEdit->text().toStdString();
	double imageClarityLevel = this->imageClarityLevelSpinner->value();
	double quantity = this->quantitySpinner->value();
	try
	{
		this->service.add_evidence(id, measurement, imageClarityLevel, quantity, photograph);
		this->populate_evidences_list();
		int lastElement = this->service.get_evidences().size() - 1;
		this->evidencesList->setCurrentRow(lastElement);
	}
	catch (const exception& exception)
	{
		QMessageBox::critical(this, "Error", exception.what());
	}
}

void GUI::delete_evidence()
{
	int selectedIndex = this->get_selected_index();
	if (selectedIndex < 0)
	{
		QMessageBox::critical(this, "Error", "No evidence was selected!");
		return;
	}
	string id = this->service.get_evidences()[selectedIndex].get_id();
	this->service.delete_evidence(id);
	this->populate_evidences_list();
}

void GUI::update_evidence()
{
	string id = this->idLineEdit->text().toStdString();
	string measurement = this->measurementsLineEdit->text().toStdString();
	string photograph = this->photographLineEdit->text().toStdString();
	double imageClarityLevel = this->imageClarityLevelSpinner->value();
	double quantity = this->quantitySpinner->value();
	try
	{
		this->service.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);
		int selectedIndex = this->get_selected_index();
		this->populate_evidences_list();
		
		if (selectedIndex < 0)
			return;
		this->evidencesList->setCurrentRow(selectedIndex);
	}
	catch (const exception& exception)
	{
		QMessageBox::critical(this, "Error", exception.what());
	}
}

void GUI::filter_evidences()
{
	
	QHBoxLayout* generalLayout = new QHBoxLayout{this->filterWidget};

	QVBoxLayout* leftLayout = new QVBoxLayout{};

	QFormLayout* filterForm = new QFormLayout{};
	QLineEdit* filterMeasurementsLineEdit = new QLineEdit{};
	QLabel* measuremntsLabel = new QLabel{ "&Measurements:" };
	measuremntsLabel->setBuddy(filterMeasurementsLineEdit);
	QDoubleSpinBox* filterQuantitySpinner = new QDoubleSpinBox{};
	QLabel* quantityLabel = new QLabel{ "&Quantity:" };
	quantityLabel->setBuddy(filterQuantitySpinner);
	filterForm->addRow(measuremntsLabel, filterMeasurementsLineEdit);
	filterForm->addRow(quantityLabel, filterQuantitySpinner);

	QPushButton* filterButton = new QPushButton("Get evidences");

	leftLayout->addLayout(filterForm);
	leftLayout->addWidget(filterButton);

	QListWidget* filteredEvidencesList = new QListWidget{};

	generalLayout->addLayout(leftLayout);
	generalLayout->addWidget(filteredEvidencesList);
	this->filterWidget->show();

	QObject::connect(filterButton, &QPushButton::clicked, [this, filterMeasurementsLineEdit, filterQuantitySpinner, filteredEvidencesList]() {

		string measurement = filterMeasurementsLineEdit->text().toStdString();
		if (measurement.size() == 0)
			measurement = "";
		double quantity = filterQuantitySpinner->value();
		if (quantity == 0)
			quantity = -1;
		filteredEvidencesList->clear();
		vector<Evidence> evidences = this->service.filter_evidences_by_measurement_and_quantity(measurement, quantity);
		for (auto evidence : evidences)
			filteredEvidencesList->addItem(QString::fromStdString(evidence.toString()));
	});

}

void GUI::set_chart()
{
	auto evidences = this->service.get_evidences();
	vector<QString> measurements;
	vector<int> number_of_evidences;
	for (auto evidence : evidences)
	{
		bool found_measurement = false;
		for (auto measurement : measurements)
			if (QString::fromStdString(evidence.get_measurement()) == measurement)
				found_measurement = true;
		if (!found_measurement)
			measurements.push_back(QString::fromStdString(evidence.get_measurement()));
	}
	for (int i = 0; i < measurements.size(); ++i)
		number_of_evidences.push_back(0);
	for (int i = 0; i < measurements.size(); ++i)
	{
		for (int j = 0; j < evidences.size(); ++j)
			if (evidences[j].get_measurement() == measurements[i].toStdString())
				number_of_evidences[i] += 1;
	}
	QBarSet* set = new QBarSet("Number of evidences");

	for (auto number : number_of_evidences)
		*set << number;

	this->chart->removeAllSeries();

	QBarSeries* series = new QBarSeries();
	series->append(set);

	chart->addSeries(series);
	chart->removeAxis(chart->axisX());
	chart->removeAxis(chart->axisY());

	QStringList measurements_list;
	for (auto measurement : measurements)
		measurements_list << measurement;
	QBarCategoryAxis* axisX = new QBarCategoryAxis();
	axisX->append(measurements_list);
	chart->addAxis(axisX, Qt::AlignBottom);
	series->attachAxis(axisX);

	QValueAxis* axisY = new QValueAxis();
	axisY->setRange(0, 10);
	axisY->setTickCount(10);
	axisY->applyNiceNumbers();
	axisY->setLabelFormat("%i");
	chart->addAxis(axisY, Qt::AlignLeft);
	series->attachAxis(axisY);
}

void GUI::select_files_window()
{
	this->selectFiles = new QWidget{};
	QVBoxLayout* selectFilesLayout = new QVBoxLayout{ selectFiles };
	QFormLayout* selectFilesForm = new QFormLayout{ };
	QPushButton* startButton = new QPushButton("Start");

	QLineEdit* repositoryFileLineEdit = new QLineEdit{};
	QLabel* repositoryFileLabel = new QLabel{ "file location:" };
	repositoryFileLabel->setBuddy(repositoryFileLineEdit);
	QLineEdit* mylistFileLineEdit = new QLineEdit{};
	QLabel* mylistFileLabel = new QLabel{ "mylist location:" };
	repositoryFileLabel->setBuddy(repositoryFileLineEdit);
	selectFilesForm->addRow(repositoryFileLabel, repositoryFileLineEdit);
	selectFilesForm->addRow(mylistFileLabel, mylistFileLineEdit);
	selectFilesLayout->addLayout(selectFilesForm);
	selectFilesLayout->addWidget(startButton);


	QObject::connect(startButton, &QPushButton::clicked, [this, repositoryFileLineEdit, mylistFileLineEdit]() {

		string repositoryFile = repositoryFileLineEdit->text().toStdString();
		if (repositoryFile.size() == 0)
		{
			QMessageBox::critical(this->selectFiles, "Error", "Must choose a file for repository!");
			return;
		}
		string mylistFile = mylistFileLineEdit->text().toStdString();
		if (mylistFile.size() == 0)
		{
			QMessageBox::critical(this->selectFiles, "Error", "Must choose a file for physical copies!");
			return;
		}
		service.set_repository_file(repositoryFile);
		if (mylistFile.find(".csv") != std::string::npos || mylistFile.find(".txt") != std::string::npos)
		{
			CSVRepository* physicalCopiesRepositoryCSV = new CSVRepository;
			this->service.set_physical_copies_repository(physicalCopiesRepositoryCSV);
		}
		else
		{
			HTMLRepository* physicalCopiesRepositoryHTML = new HTMLRepository;
			this->service.set_physical_copies_repository(physicalCopiesRepositoryHTML);
		}
		this->service.set_physical_copies_file(mylistFile);
		this->selectFiles->hide();
		this->populate_evidences_list();
		this->show();
	});
}

void GUI::init_gui()
{
	this->filterWidget = new QWidget{};
	this->evidencesWidget = new QWidget{};
	this->chartWidget = new QWidget{};

	QHBoxLayout* chartLayout = new QHBoxLayout{ this->chartWidget };
	this->addTab(evidencesWidget, "All evidences");
	this->addTab(this->chartWidget, "Chart");
	this->chart = new QChart();
	this->chartView = new QChartView(chart);
	chart->setTitle("Measurements report");
	chart->setAnimationOptions(QChart::SeriesAnimations);
	chart->legend()->setVisible(true);
	chart->legend()->setAlignment(Qt::AlignBottom);
	chartView->setRenderHint(QPainter::Antialiasing);
	chartLayout->addWidget(this->chartView);


	//general layout
	QHBoxLayout* generalLayout = new QHBoxLayout{ this->evidencesWidget };

	//left side
	QVBoxLayout* leftLayout = new QVBoxLayout{};

	//label
	QLabel* labelEvidencesList = new QLabel{ "All evidences" };
	
	//evidences list
	this->evidencesList = new QListWidget{};
	
	//evidence form
	QFormLayout* evidenceForm = new QFormLayout{};
	
	this->idLineEdit = new QLineEdit{};
	QLabel* idLabel = new QLabel{ "&Id:" };
	idLabel->setBuddy(this->idLineEdit);

	this->measurementsLineEdit = new QLineEdit{};
	QLabel* measumentsLabel = new QLabel{ "&Measurements:" };
	measumentsLabel->setBuddy(this->measurementsLineEdit);

	this->imageClarityLevelSpinner = new QDoubleSpinBox{};
	QLabel* imageClarityLevelLabel = new QLabel{ "&Image clarity level:" };
	imageClarityLevelLabel->setBuddy(this->imageClarityLevelSpinner);

	this->quantitySpinner = new QDoubleSpinBox{};
	QLabel* quantityLabel = new QLabel{ "&Quantity:" };
	quantityLabel->setBuddy(this->quantitySpinner);

	this->photographLineEdit = new QLineEdit;
	QLabel* photographLabel = new QLabel{ "&Phototgraph:" };
	photographLabel->setBuddy(this->photographLineEdit);

	evidenceForm->addRow(idLabel, this->idLineEdit);
	evidenceForm->addRow(measumentsLabel, this->measurementsLineEdit);
	evidenceForm->addRow(imageClarityLevelLabel, this->imageClarityLevelSpinner);
	evidenceForm->addRow(quantityLabel, this->quantitySpinner);
	evidenceForm->addRow(photographLabel, this->photographLineEdit);

	//buttons
	QGridLayout* evidencesButtons = new QGridLayout{};
	this->addEvidenceButton = new QPushButton("Add");
	this->deleteEvidenceButton = new QPushButton("Delete");
	this->updateEvidenceButton = new QPushButton("Update");
	this->filterEvidencesButton = new QPushButton("Filter");

	evidencesButtons->addWidget(addEvidenceButton, 0, 0);
	evidencesButtons->addWidget(deleteEvidenceButton, 0, 1);
	evidencesButtons->addWidget(updateEvidenceButton, 0, 2);
	evidencesButtons->addWidget(filterEvidencesButton, 1, 1);

	//add to the left layout
	leftLayout->addWidget(labelEvidencesList);
	leftLayout->addWidget(this->evidencesList);
	leftLayout->addLayout(evidenceForm);
	leftLayout->addLayout(evidencesButtons);

	//save button
	this->saveEvidenceButton = new QPushButton(">");

	//right side
	QVBoxLayout* rightLayout = new QVBoxLayout{};

	//label
	QLabel* labelCopiesList = new QLabel{ "Physical copies" };

	//physical copies list
	this->physicalCopiesList = new QListWidget{};

	//physical copies buttons
	this->nextEvidenceButton = new QPushButton("Next");

	rightLayout->addWidget(labelCopiesList);
	rightLayout->addWidget(this->physicalCopiesList);
	rightLayout->addWidget(this->nextEvidenceButton);

	//add everything to the general layout
	generalLayout->addLayout(leftLayout);
	generalLayout->addWidget(this->saveEvidenceButton);
	generalLayout->addLayout(rightLayout);
}