jury = int(input())
presentation_counter = 0
final_grade = 0

input_line = input()

while input_line != "Finish":
    current_presentation_name = input_line
    presentation_counter += 1
    current_presentation_grade = 0

    for i in range(jury):
        mark = float(input())
        current_presentation_grade += mark

    avg_grade = current_presentation_grade / jury
    print(f"{current_presentation_name} - {avg_grade:.2f}.")
    final_grade += avg_grade
    input_line = input()
final_avg_grade = final_grade / presentation_counter

print(f"Student's final assessment is {final_avg_grade:.2f}.")
