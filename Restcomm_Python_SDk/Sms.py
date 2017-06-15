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

import requests
import json

class client(object):

    def __init__(self, Sid, AuthToken, BaseUrl):

        self.Sid = Sid
        self.AuthToken = AuthToken
        self.BaseUrl = BaseUrl

class SendSms(object):

    def __init__(self, To, From, Body, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.To = To
        self.From = From
        self.Body = Body

    def Send(self):

        BaseUrl = self.BaseUrl+'/Accounts/'+self.Sid+'/SMS/Messages.json'
        data = {'To': self.To, 'From': self.From, 'Body': self.Body}
        r1 = requests.post(BaseUrl, data=data, auth=(self.Sid, self.AuthToken))

        content = json.loads(r1.text)
        return content

class SmsList(object):

    def __init__(self, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def GetList(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/SMS/Messages.json'
        r2 = requests.get(Url, auth=(self.Sid, self.AuthToken))

        content = json.loads(r2.text)
        return content

class FilterSmsList(object):

    def __init__(self, FilterNumber, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.FilterNumber = FilterNumber

    def GetFilterlist(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/SMS/Messages.json'
        params = {'From': self.FilterNumber}
        r3 = requests.get(Url, params=params, auth=(self.Sid, self.AuthToken))

        content = json.loads(r3.text)
        return content

class SmsPagingInformation(object):

    def __init__(self, PageSize, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.PageSize = PageSize

    def PageInfo(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/SMS/Messages.json'
        params = {'PageSize': self.PageSize}
        r4 = requests.get(Url, params=params, auth=(self.Sid, self.AuthToken))

        content = json.loads(r4.text)
        return content