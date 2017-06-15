'''
 * TeleStax, Open Source Cloud Communications
 * Copyright 2011-2017, Telestax Inc and individual contributors
 * by the @authors tag.
 *
 * This program is free software: you can redistribute it and/or modify
 * under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation; either version 3 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>
 '''

from Restcomm_Python_SDk import Email
import unittest
import requests
from unittest.mock import Mock, patch

class TestEmail(unittest.TestCase):

    def test_SendMail(self):

        try:

            with patch.object(requests, 'get')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Email>
                           <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                           <status>completed</status>
                           <DateCreated>12/06/2017</DateCreated>
                           <DateUpdated>15/06/2017</DateUpdated>
                           </Email>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')
                file = open("EmailData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                To = file.readline()
                From = file.readline()
                Subject = file.readline()
                Body = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = Email.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Email.SendEmail(To.strip(), From.strip(), Subject.strip(), Body.strip(), data).Send()
                self.assertIsNotNone(content)
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect! or you have an incorrect Email ID3")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

if __name__=="__main__":

    unittest.main()

