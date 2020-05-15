#pragma once
#include <qwidget.h>
#include "Evidence.h"
#include "Service.h"
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QPushButton>
#include <QLabel>
#include <QSlider>
#include <QSpinBox>
#include <QDoubleSpinBox>
#include <QtWidgets/QMainWindow>
#include <QtCharts/QChartView>
#include <QtCharts/QBarSeries>
#include <QtCharts/QBarSet>
#include <QtCharts/QLegend>
#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QValueAxis>
#include <QtCharts/QHorizontalBarSeries>

QT_CHARTS_USE_NAMESPACE


class GUI : public QTabWidget
{
	Q_OBJECT
private:
	Service& service;
	QWidget* evidencesWidget;
	QWidget* chartWidget;
	QChart* chart;
	QChartView* chartView;
	QListWidget* evidencesList;
	QListWidget* physicalCopiesList;
	QLineEdit* idLineEdit;
	QLineEdit* measurementsLineEdit;
	QLineEdit* photographLineEdit;
	QDoubleSpinBox* imageClarityLevelSpinner;
	QDoubleSpinBox* quantitySpinner;
	QPushButton* addEvidenceButton;
	QPushButton* deleteEvidenceButton;
	QPushButton* updateEvidenceButton;
	QPushButton* filterEvidencesButton;
	QPushButton* saveEvidenceButton;
	QPushButton* nextEvidenceButton;
	QWidget* filterWidget;

	void init_gui();
public:
	QWidget* selectFiles;
	GUI(Service& service);
	void populate_evidences_list();
	void connect_signal_and_slots();

	int get_selected_index() const;
	void add_evidence();
	void delete_evidence();
	void update_evidence();
	void filter_evidences();
	void set_chart();

	void select_files_window();
};

