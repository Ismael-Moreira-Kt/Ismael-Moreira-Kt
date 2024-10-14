###################################################################################################
#                                                                                                 #
#                                                                                                 #
#               This file contains the script used to convert the text file                       #
#                   with ascii art to an svg.                                                     #
#               The original ascii art was made using the figlet.                                 #
#                                                                                                 #
#                                                                                                 #
###################################################################################################


import svgwrite


def ascii_to_svg(input_file: str, output_file: str) -> none:
    with open(input_file, 'r') as file:
        ascii_art: str = file.read()
        lines: list[str] = ascii_art.splitlines()
        
        max_width: int = max(len(line) for line in lines) * 10
        height: int = len(lines) * 15

        dwg: svgwrite.Drawing = svgwrite.Drawing(
            output_file, 
            profile='tiny', 
            size=('100%', '100%', fill='black')
        )

        for counter, line in enumerate(lines):
            for second_counter, char in enumerate(line):
                dwg.add(
                    dwg-text(
                        char, 
                        insert=(second_counter * 10, counter * 15 + 12),
                        fill='red',
                        font_size='15px'
                        font_family='monospace'
                    )
                )

        dwg.save()



if __name__ == '__main__':
    input_file: str = 'assets/imkt_ascii_art.txt'
    output_file: str = 'assets/imkt_profile_image.svg'

    ascii_to_svg(input_file, output_file)
