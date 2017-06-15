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

from Restcomm_Python_SDk import AccountInfo
import unittest
import requests
from unittest.mock import Mock, patch

class TestAccountDetails(unittest.TestCase):

    def test_details(self):

        try:

            with patch.object(requests, 'get')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Account>
                <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                <status>Active</status>
                <Role>Administrator</Role>
                <DateCreated>12/06/2017</DateCreated>
                <DateUpdated>15/06/2017</DateUpdated>
                </Account>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')
                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.AccountDetails(data).Details()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: AccountSid or AuthToken is incorrect!")
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


class TestChangeAccountPassword(unittest.TestCase):

    def test_Password(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Account>
                           <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                           <status>Active</status>
                           <Role>Administrator</Role>
                           <DateCreated>12/06/2017</DateCreated>
                           <DateUpdated>15/06/2017</DateUpdated>
                           <AuthToken>3awq2847a1fwlcm43ae968b33f9dlay3</AuthToken>
                           </Account>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')
                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                Password = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.ChangeAccountPassword(Password.strip(), data).ChangePassword()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: AccountSid or AuthToken is incorrect!")
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

class TestCreateSubAccount(unittest.TestCase):

    def test_Create(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Account>
                           <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                           <status>Active</status>
                           <Role>Administrator</Role>
                           <DateCreated>12/06/2017</DateCreated>
                           <DateUpdated>15/06/2017</DateUpdated>
                           </Account>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')
                file = open("AccountData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                Password = file.readline()
                FriendlyName = file.readline()
                Email = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.CreateSubAccount(FriendlyName.strip(), Email.strip(), Password.strip(), data)
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems like your Username/Email-ID is already in use. Please also check your AccountSid/AuthToken!")
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

class TestCloseSubAccount(unittest.TestCase):

    def test_Close(self):

        try:

            with patch.object(requests, 'post')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Account>
                           <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                           <status>closed</status>
                           <Role>Administrator</Role>
                           <DateCreated>12/06/2017</DateCreated>
                           <DateUpdated>15/06/2017</DateUpdated>
                           </Account>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                SubSid = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()

                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl)
                content = AccountInfo.CloseSubAccount(SubSid.strip(), data).Close()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems like your Username/Email-ID is already in use. Please also check your AccountSid/AuthToken!")
        except ConnectionError:
            print("Syntax Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Syntax Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestSubAccountDetails(unittest.TestCase):

    def test_Details(self):

        try:

            with patch.object(requests, 'get')as get_mock:

                file2 = open('index.html', 'w')

                message = """<Accounts>
                             <Account>
                           <sid>QW21b4d94a9b2b1862342a1978b70d26f2</sid>
                           <status>closed</status>
                           <Role>Administrator</Role>
                           <DateCreated>12/06/2017</DateCreated>
                           <DateUpdated>15/06/2017</DateUpdated>
                           </Account>
                           </Accounts>"""

                file2.write(message)
                file2.close()

                file2 = open('index.html', 'r')

                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                get_mock.return_value = mock_response = Mock()
                mock_response = file2.read()
                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.SubAccountDetails(data).Details()
                self.assertEqual(content, file2.read())
                self.assertIsNotNone(content)
                file.close()
                file2.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems like your Username/Email-ID is already in use. Please also check your AccountSid/AuthToken!")
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

if __name__=="__main__":
    unittest.main()
