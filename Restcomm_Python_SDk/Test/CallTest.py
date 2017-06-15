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

from Restcomm_Python_SDk import call
import unittest
import requests
from unittest.mock import Mock, patch

class TestMakeCall(unittest.TestCase):

    def testCall(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Call>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <DateCreated>12/06/2017</DateCreated>
                <DateUpdated>15/06/2017</DateUpdated>
                </Call>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("CallData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                From = file.readline()
                To = file.readline()
                Url = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.Makecall(From.strip(), To.strip(), Url.strip(), data).Call()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
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
        except IndexError:
            print("Index Error: list Index out of range")

class TestGetCallDetails(unittest.TestCase):

    def test_GetDetails(self):

        try:

            with patch.object(requests, 'get')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Call>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <DateCreated>12/06/2017</DateCreated>
                <DateUpdated>15/06/2017</DateUpdated>
                </Call>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("CallData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.GetCallDetail(data).GetDetails()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("TypeError: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestRedirectCall(unittest.TestCase):

    def test_Redirect(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Call>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <DateCreated>12/06/2017</DateCreated>
                <DateUpdated>15/06/2017</DateUpdated>
                </Call>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("CallData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                Url = file.readline()
                SubSid = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.RedirectCall(Url, SubSid, data).Redirect()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("TimeoutError: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestConferenceCall(unittest.TestCase):

    def test_Conference(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Call>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <DateCreated>12/06/2017</DateCreated>
                <DateUpdated>15/06/2017</DateUpdated>
                </Call>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("CallData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                Url = file.readline()
                SubSid = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.ConferenceCall(Url, SubSid, data).Conference()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
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
        except IndexError:
            print("Index Error: list Index out of range")

class TestMuteCall(unittest.TestCase):

    def test_Mute(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Call>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <DateCreated>12/06/2017</DateCreated>
                <DateUpdated>15/06/2017</DateUpdated>
                </Call>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("CallData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                PartSid = file.readline()
                ConSid = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.MuteParticipant(PartSid, ConSid, data).Mute()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
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
        except IndexError:
            print("Index Error: list Index out of range")


class TestUnMuteCall(unittest.TestCase):
    def test_Mute(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Call>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <DateCreated>12/06/2017</DateCreated>
                <DateUpdated>15/06/2017</DateUpdated>
                </Call>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("CallData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                PartSid = file.readline()
                ConSid = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = call.client(Sid.strip(), AuthToken.strip())
                content = call.UnMuteParticipant(PartSid, ConSid, data).UnMute()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
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
        except IndexError:
            print("Index Error: list Index out of range")

if __name__ == '__main__':
    unittest.main()