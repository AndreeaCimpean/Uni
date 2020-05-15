#pragma once
#include <vector>
#include "TextFileRepository.h"

using namespace std;

class HTMLRepository : public TextFileRepository
{
public:
	std::vector<Evidence> get_evidences_from_file() const override;
	void save_evidences_to_file(std::vector<Evidence> physicalCopies) const override;
	void write_html_header() const;
	void write_html_body_begin() const;
	void write_html_body_end() const;
	void add_evidence(const Evidence& evidence) override;
};

