#include <stdio.h>

int main()
{
    char message[100];
    scanf("%[^\n]s", message);
    printf(message);
    return 0;
}