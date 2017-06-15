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

class Makecall(object):

    def __init__(self, From, To, Url, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.From = From
        self.To = To
        self.Url = Url

    def Call(self):

        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/Calls.json'
        data = {'From': self.From, 'To': self.To, 'Url': self.Url}

        r1 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

        content = json.loads(r1.text)
        return content

class GetCallDetail(object):

    def __init__(self, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def GetDetails(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Calls.json'
        r2 = requests.get(Url, auth=(self.Sid, self.AuthToken))

        content = json.loads(r2.text)
        return content

class RedirectCall(object):

    def __init__(self, Url, SubSid, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.Url = Url
        self.SubSid = SubSid

    def Redirect(self):

        data = {'Url': self.Url}
        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Calls.json/'+self.SubSid
        r3 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))

        content = json.loads(r3.text)
        return content

class ConferenceCall(object):

    def __init__(self, sig_Url, SubSid, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.SubSid = SubSid
        self.sig_Url = sig_Url

    def Conference(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Calls.json/' + self.SubSid
        data = {'Url': self.sig_Url, 'MoveConnectedCallLeg': 'true'}

        r4 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))
        content = json.loads(r4.text)
        return content

class MuteParticipant(object):

    def __init__(self, ParticipantSid, ConferenceSid, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.ParticipantSid = ParticipantSid
        self.ConferenceSid = ConferenceSid

    def Mute(self):

        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Conferences.json/' + self.ConferenceSid + '/Participants/' + self.ParticipantSid
        data = {'Mute': 'true'}

        r5 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))
        content = json.loads(r5.text)
        return content

class UnMuteParticipant(object):

    def __init__(self, ParticipantSid, ConferenceSid, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.ParticipantSid = ParticipantSid
        self.ConferenceSid = ConferenceSid

    def UnMute(self):
        Url = self.BaseUrl+'/Accounts/' + self.Sid + '/Conferences.json/' + self.ConferenceSid + '/Participants/' + self.ParticipantSid
        data = {'Mute': 'false'}

        r6 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))
        content = json.loads(r6.text)
        return content