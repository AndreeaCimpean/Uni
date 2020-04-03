#include <stdio.h>

typedef struct {
	int x;
	int y;
} Point;

float slope_of_line_formed_by_two_points(Point point1, Point point2)
{
	return ((float)point2.y - point1.y) / ((float)point2.x - point1.x);
}

int main()
{
	int number_of_points = 0;
	Point points[100];
	char delimiter_character = 'a';

	//read coordinates
	while (delimiter_character != '\n')
	{
		scanf("%d%c", &points[number_of_points].x, &delimiter_character);
		scanf("%d%c", &points[number_of_points].y, &delimiter_character);
		number_of_points += 1;
	}

	/*
	for (int j = 0; j < number_of_points; ++j)
	{
		printf(" %d ", points[j].x);
		printf("%d    ", points[j].y);
	}*/

	// find the longest contiguous subsequence with the points on the same line

	int max_length = 1, start_position_max = 0, end_position_max = 1;

	float current_slope = slope_of_line_formed_by_two_points(points[0], points[1]);
	int  index = 2, current_length = 1, current_start_position = 0, current_end_position = 1;

	while (index < number_of_points)
	{
		if (slope_of_line_formed_by_two_points(points[index], points[index-1]) == current_slope)
		{
			current_end_position = index;
			current_length += 1;
		}
		else
		{
			if (current_length > max_length)
			{
				max_length = current_length;
				start_position_max = current_start_position;
				end_position_max = current_end_position;
			}
			current_slope = slope_of_line_formed_by_two_points(points[index - 1], points[index]);
			current_length = 1;
			current_start_position = index - 1;
			current_end_position = index;
		}
		index += 1;
	}
	if (current_length > max_length)
	{
		max_length = current_length;
		start_position_max = current_start_position;
		end_position_max = current_end_position;
	}

	//print the longest sequence
	printf("%d ", points[start_position_max].x);
	printf("%d", points[start_position_max].y);
	for (int i = start_position_max + 1; i <= end_position_max; ++i)
	{
		printf(" %d ", points[i].x);
		printf("%d", points[i].y);
	}
	return 0;
}