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

from Restcomm_Python_SDk.Restcomm.Email import Email


class TestEmail(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_SendMail(self):

        try:
                Sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                AuthToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                BaseUrl = 'https://mockServer.com/mock/2012-04-24'
                To = 'sma23ze@gmail.com'
                From = 'hunwqqd@gmail.com'
                Subject = 'Demo'
                Body = 'Hey! how r u?'

                data = Email.client(Sid, AuthToken, BaseUrl)
                content = Email.SendEmail(To, From, Subject, Body, data).Send()
                self.assertIsNotNone(content)

        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

if __name__=="__main__":

    unittest.main()

