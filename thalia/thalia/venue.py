from thalia.section import Sections


class Theater:
    """Theater/Seating section."""
    theater = [{"section_name": "Front right",
                "seating": [{
                    "row": "1",
                    "seats": ["1", "2", "3", "4"]
                },
                    {"row": "2",
                     "seats": ["1", "2", "3", "4"]
                     },
                    {"row": "3",
                     "seats": ["1", "2", "3", "4"]
                     },
                    {"row": "4",
                     "seats": [
                         "1",
                         "2",
                         "3",
                         "4"
                     ]
                     }
                ]
                },
               {
                   "section_name": "Front center",
                   "seating": [{
                       "row": "1",
                       "seats": [
                           "5",
                           "6",
                           "7",
                           "8"
                       ]
                   },
                       {
                           "row": "2",
                           "seats": [
                               "5",
                               "6",
                               "7",
                               "8"
                           ]
                       },
                       {
                           "row": "3",
                           "seats": [
                               "5",
                               "6",
                               "7",
                               "8",
                               "9"
                           ]
                       },
                       {
                           "row": "4",
                           "seats": [
                               "5",
                               "6",
                               "7",
                               "8",
                               "9",
                               "10"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Front left",
                   "seating": [{
                       "row": "1",
                       "seats": [
                           "9",
                           "10",
                           "11",
                           "12"
                       ]
                   },
                       {
                           "row": "2",
                           "seats": [
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       },
                       {
                           "row": "3",
                           "seats": [
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       },
                       {
                           "row": "4",
                           "seats": [
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Main right",
                   "seating": [{
                       "row": "5",
                       "seats": [
                           "1",
                           "2",
                           "3",
                           "4",
                           "5"
                       ]
                   },
                       {
                           "row": "6",
                           "seats": [
                               "1",
                               "2",
                               "3",
                               "4",
                               "5"
                           ]
                       },
                       {
                           "row": "7",
                           "seats": [
                               "1",
                               "2",
                               "3",
                               "4",
                               "5"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Main center",
                   "seating": [{
                       "row": "5",
                       "seats": [
                           "6",
                           "7",
                           "8",
                           "9",
                           "10",
                           "11"
                       ]
                   },
                       {
                           "row": "6",
                           "seats": [
                               "6",
                               "7",
                               "8",
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       },
                       {
                           "row": "7",
                           "seats": [
                               "6",
                               "7",
                               "8",
                               "9",
                               "10",
                               "11",
                               "12",
                               "13"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Main left",
                   "seating": [{
                       "row": "5",
                       "seats": [
                           "12",
                           "13",
                           "14",
                           "15",
                           "16"
                       ]
                   },
                       {
                           "row": "6",
                           "seats": [
                               "13",
                               "14",
                               "15",
                               "16",
                               "17"
                           ]
                       },
                       {
                           "row": "7",
                           "seats": [
                               "14",
                               "15",
                               "16",
                               "17",
                               "18"
                           ]
                       }
                   ]
               }
               ]

    def __init__(self):
        self.__theater = list()
        self.create_theater(self.theater)

    def get_theater(self):
        return self.__theater

    def create_theater(self, theater_json):
        """theater is a list of"""
        for section in theater_json:
            new_seating = Sections(name=section['section_name'], row=section['seating'])
            self.__theater.append(new_seating)
