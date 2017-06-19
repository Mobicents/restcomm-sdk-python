'''
 * TeleStax, Open Source Cloud Communications
 * Copyright 2011-2016, Telestax Inc and individual contributors
 * by the @authors tag.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 '''

from Restcomm_Python_SDk import Client
import unittest
import vcr


class TestCreateClient(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Create(self):

        try:

            file = open("ClientData.txt", "r")
            Sid = file.readline()
            AuthToken = file.readline()
            BaseUrl = file.readline()
            Login = file.readline()
            Password = file.readline()

            data = Client.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
            content = Client.CreateClient(Login.strip(), Password.strip(), data).Create()

            self.assertIsNotNone(content)
            file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect!")
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


class DeleteClient(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Delete(self):

        try:

            file = open("ClientData.txt", "r")
            Sid = file.readline()
            AuthToken = file.readline()
            BaseUrl = file.readline()
            file.readline()
            file.readline()
            ClientSid = file.readline()

            data = Client.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
            content = Client.DeleteClient(ClientSid.strip(), data).Delete()

            self.assertIsNotNone(content)
            file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect!")
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


class TestChangePassword(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Change(self):

        try:

            file = open("ClientData.txt", "r")
            Sid = file.readline()
            AuthToken = file.readline()
            BaseUrl = file.readline()
            file.readline()
            file.readline()
            ClientSid = file.readline()
            Password = file.readline()

            data = Client.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
            content = Client.ChangeClientPassword(ClientSid.strip(), Password.strip(), data).ChangePassword()

            self.assertIsNotNone(content)
            file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect!")
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


class TestClientList(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_list(self):

        try:

            file = open("ClientData.txt", "r")
            Sid = file.readline()
            AuthToken = file.readline()
            BaseUrl = file.readline()

            data = Client.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
            content = Client.ClientList(data).GetList()

            self.assertIsNotNone(content)
            file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect!")
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