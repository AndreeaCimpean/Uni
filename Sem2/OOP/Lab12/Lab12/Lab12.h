#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_Lab12.h"

class Lab12 : public QMainWindow
{
	Q_OBJECT

public:
	Lab12(QWidget *parent = Q_NULLPTR);

private:
	Ui::Lab12Class ui;
};
