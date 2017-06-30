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

import vcr

from Restcomm_Python_SDk.Restcomm.Applications import Applications


class TestCreateApplication(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Create(self):

        try:

                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'
                FriendlyName = 'dummy'
                kind = 'voice'

                data = Applications.client(Sid, AuthToken, BaseUrl)
                content = Applications.CreateApplication(FriendlyName, kind, data).Create()

                self.assertIsNotNone(content)
                self.assertNotEqual(Sid, content["sid"])

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestGetApplicationDetail(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_GetDetail(self):

        try:
                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'

                data = Applications.client(Sid, AuthToken, BaseUrl)
                content = Applications.GetApplicationList(data).GetList()

                self.assertIsNotNone(content)

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except IndexError:
            print("Index Error: list Index out of range")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestUpdateApplication(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Update(self):

        try:

                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'
                FriendlyName = 'dummy21'
                AppSid = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

                data = Applications.client(Sid, AuthToken, BaseUrl)
                content = Applications.UpdateApplication(AppSid, FriendlyName, data).Update()

                self.assertIsNotNone(content)

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type!")

class TestDeleteApplication(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Delete(self):

        try:
                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'
                AppSid = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

                data = Applications.client(Sid, AuthToken, BaseUrl)
                content = Applications.DeleteApplication(AppSid, data).Delete()
                self.assertEqual(content, "Deleted")

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

if __name__=="__main__":
    unittest.main()
