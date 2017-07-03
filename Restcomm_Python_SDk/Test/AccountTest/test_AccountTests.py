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
 
 This code was generated by :
 Name: Md Sharique
 Email : nukles1.07@gmail.com
 '''

import unittest
import nose
import vcr
from Restcomm_Python_SDk.Restcomm.Account import AccountInfo


class TestAccountDetails(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_details(self):

        try:

                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'

                data = AccountInfo.client(Sid, AuthToken, BaseUrl)
                content = AccountInfo.AccountDetails(data).Details()
                self.assertIsNotNone(content)
                self.assertEqual(Sid, content["sid"])

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")


class TestChangeAccountPassword(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Password(self):

        try:

                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'
                Password = 'dummyPassword1234'

                data = AccountInfo.client(Sid, AuthToken, BaseUrl)
                content = AccountInfo.ChangeAccountPassword(Password, data).ChangePassword()

                self.assertIsNotNone(content)
                self.assertNotEqual(AuthToken, content['auth_token'])

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestCreateSubAccount(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Create(self):

        try:

                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'
                Password = 'dummyPassword345'
                FriendlyName = 'NoOne'
                Email = 'NoOne31@gmail.com'

                data = AccountInfo.client(Sid, AuthToken, BaseUrl)
                content = AccountInfo.CreateSubAccount(FriendlyName, Email, Password, data).Create()
                self.assertIsNotNone(content)
                self.assertEqual(content["status"], "active")
                self.assertNotEqual(AuthToken, content["auth_token"])
                self.assertNotEqual(Sid, content["sid"])

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestCloseSubAccount(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Close(self):

        try:

                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'
                SubSid = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

                data = AccountInfo.client(Sid, AuthToken, BaseUrl)
                content = AccountInfo.CloseSubAccount(SubSid, data).Close()

                self.assertIsNotNone(content)
                self.assertEqual(content["status"], 'closed')

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestSubAccountDetails(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Details(self):

        try:
                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'

                data = AccountInfo.client(Sid, AuthToken, BaseUrl)
                content = AccountInfo.SubAccountDetails(data).Details()

                self.assertIsNotNone(content)

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
    nose.main()

