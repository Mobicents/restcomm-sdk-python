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

#import Restcomm_Python_SDK to use its features
import Restcomm_Python_SDk

#Take the AccountSid, Authentication Token & Base Url from the user

AccountSid = input("Enter the AccountSid here:")
AuthToken = input("Enter the Authentication Token here:")
BaseUrl = input("Enter the Base url here:")

#call the client class to enter Account Sid and Authentication Token

client = Restcomm_Python_SDk.client(AccountSid, AuthToken, BaseUrl)

def AccountExamples():

    #To get Details of the Account, call 'AccountDetails' class and then call 'Detail' function

    getInfo = Restcomm_Python_SDk.AccountDetails(client).Details()
    print("Details of the Account with given Account Sid and Auth Token are: ")
    print(getInfo)

    #To change Account Password, call 'ChangeAccountPassword' class and then call 'ChangePassword' function

    Password1 = input("Enter the new Password here:")
    changePass = Restcomm_Python_SDk.ChangeAccountPassword(Password1, client).ChangePassword()
    print("Details of the Account with new Authentication Token are: ")
    print(changePass)

    #To create Sub Account, call 'CreateSubAccount' class and then call 'Create' function

    FriendlyName = input("Enter the Friendly Name here")
    Email = input("Enter the Email Address here")
    Password2 = input("Enter the Password here")

    createSub = Restcomm_Python_SDk.CreateSubAccount(FriendlyName, Email, Password2, client).Create()
    print("Details of the Sub Account Created")
    print(createSub)

    #To close Sub Account, call 'CloseSubAccount' class and then call 'Close' function

    SubSid = input("Enter the Sub Account Sid to close")
    closeSub = Restcomm_Python_SDk.CloseSubAccount(SubSid, client).Close()
    print(closeSub)

    #To get Details of all Sub Account, call 'SubAccountDetails' class and then call 'Details' function

    getSubInfo = Restcomm_Python_SDk.SubAccountDetails(client).Details()
    print(getSubInfo)

def ApplicationExample():

    #To Create an Application, call 'CreateApplication' class and then call 'Create'function

    FriendlyName1 = input("Enter the name of the Application here")
    kind = input("Enter the kind of Application here")
    CreateApp = Restcomm_Python_SDk.CreateApplication(FriendlyName1, kind, client).Create()
    print(CreateApp)

    #To Delete an Application, call 'DeleteApplication' class and then call 'Delete' function

    AppSid1 = input("Enter the Application Sid to delete")
    deleteApp = Restcomm_Python_SDk.DeleteApplication(AppSid1, client).Delete()
    print(deleteApp)

    #To Update an Application, call 'UpdateApplication' class and then call 'Update' function

    AppSid2 = input("Enter the Application Sid to Update")
    FriendlyName2 = input("Enter the new name of the Application to update")
    UpdateApp = Restcomm_Python_SDk.UpdateApplication(AppSid2, FriendlyName2, client).Update()
    print(UpdateApp)

    #To get list of Applications, call 'GetApplicationList' class and then call 'GetList' function

    getInfo = Restcomm_Python_SDk.GetApplicationList(client).GetList()
    print("Details of Applications are: ")
    print(getInfo)

def AvailableNumberExample():

    #to get the list of number availability, call 'NumberAvailablity' class and then call 'Availability' function

    AreaCode = input("Enter the Area Code")
    Avail = Restcomm_Python_SDk.NumberAvailablity(AreaCode, client).Availability()
    print(Avail)

def callExample():

    #To Make calls to an user, call 'MakeCall' class and then call 'call' function

    From = input("Enter your Phone Number to call")
    To = input("Enter the Phone Number of the User to make Call")
    Url = input("Enter the Url of the call")
    MakeCall = Restcomm_Python_SDk.Makecall(From, To, Url, client).Call()
    print(MakeCall)

    #To get call Details, call 'GetCallDetails' class and then call 'GetDetails' function

    getInfo = Restcomm_Python_SDk.GetCallDetail(client).GetDetails()
    print(getInfo)

    #To Redirect the Call, call 'RedirectCall' class and then call 'Redirect' function

    Url = input("Enter the Url of the Redirect call")
    SubSid = input("Enter the Sid of the client to redirect the call")
    RedirectCall = Restcomm_Python_SDk.RedirectCall(Url, SubSid, client).Redirect()
    print(RedirectCall)

    #To make a conference Call, call 'ConferenceCall' class and then call 'Conference' function

    sig_Url = input("Enter the value")
    SubSid = input("Enter the Participant Sid")
    ConfCall = Restcomm_Python_SDk.ConferenceCall(sig_Url, SubSid, client).Conference()
    print(ConfCall)

    #To Mute a participant, call 'MuteParticipant' class and then call 'Mute' function

    PartSid1 = input("Enter the Participant Sid")
    ConfSid1 = input("Enter the Conference Sid")
    Mute = Restcomm_Python_SDk.MuteParticipant(PartSid1, ConfSid1, client).Mute()
    print(Mute)

    #To Unmute a participant, call 'UnMuteParticipant' class and then call 'UnMute' function

    PartSid2 = input("Enter the Participant Sid")
    ConfSid2 = input("Enter the Conference Sid")
    UnMute = Restcomm_Python_SDk.UnMuteParticipant(PartSid2, ConfSid2, client).UnMute()
    print(UnMute)

def clientExample():

    #To Create a client, call 'CreateClient' class and then call 'Create' function

    Login = input("Enter the Login Name of the client")
    Password1 = input("Enter the Password of the client")
    created = Restcomm_Python_SDk.CreateClient(Login, Password1, client).Create()
    print(created)

    #To delete a client, call 'DeleteClient' class and then call 'Delete' function

    ClientSid1 = input("Enter the Sid of the Client")
    deleted = Restcomm_Python_SDk.DeleteClient(ClientSid1, client).Delete()
    print(deleted)

    #To change Password of a client, call 'ChangeClientPassword' class and then call 'ChangePassword' function

    ClientSid2 = input("Enter the Sid of the client")
    Password2 = input("Enter the new Password of the client")
    changePass = Restcomm_Python_SDk.ChangeClientPassword(ClientSid2, Password2, client).ChangePassword()
    print(changePass)

    #To get list of the clients, call 'ClientList' class and then call 'GetList' function
    getInfo = Restcomm_Python_SDk.ClientList(client).GetList()
    print(getInfo)

def EmailExample():

    #To send Email, call 'SendEmail' class and then call 'Send' function

    To = input("Enter the mail id of the receiver")
    From = input("Enter the mail id of the sender")
    Subject = input("Enter the subject of the message")
    Body = input("Enter the body of the message")
    sending = Restcomm_Python_SDk.SendEmail(To, From, Subject, Body, client).Send()
    print(sending)

def GatewayExample():

    #To create a Gateway, call 'CreateGateway' class and then call 'Create' function

    FriendlyName1 = input("Enter the Friendly Name")
    UserName1 = input("Enter the User Name")
    Password1 = input("Enter the Password")
    Proxy = input("Enter the Proxy")
    CreateGate = Restcomm_Python_SDk.CreateGateway(FriendlyName1, UserName1, Password1, Proxy, client).Create()
    print(CreateGate)

    #To get the list of the Gateways, call 'GetListGateway' class and then call 'GetList' function

    getInfo = Restcomm_Python_SDk.GetlistGateway(client).GetList()
    print(getInfo)

    #To update the details of a Gateway, call 'UpdateGateway' class and then call 'Update' function

    GatewaySid1 = input("Enter the Gateway Sid")
    FriendlyName2 = input("Enter the Friendly Name of the Gateway")
    UserName2 = input("Enter the UserName of the Gateway")

    UpdateGate = Restcomm_Python_SDk.UpdateGateway(GatewaySid1, FriendlyName2, UserName2, client).Update()
    print(UpdateGate)

    #To Delete a Gateway, call 'DeleteGateway' class and then call 'Delete' function

    GatewaySid2 = input("Enter the Sid of the Gateway to delete it")
    DeleteGate = Restcomm_Python_SDk.DeleteGateway(GatewaySid2, client).Delete()
    print(DeleteGate)

def NotificationExample():

    #To get list of all Notification, call 'NotificationList' class and then call 'GetList' function

    getInfo = Restcomm_Python_SDk.NotificationList(client).GetList()
    print(getInfo)

    #To get list of Filtered Notification, call 'NotificationFilter' class and then call 'FilterErrorCode' function or 'FilterPage' function

    filterlist = Restcomm_Python_SDk.NotificationFilter('1', client).FilterPage()
    print(filterlist)

def RecordingExample():

    #To get list of all Recordings, call 'RecordingList' class and then call 'GetList' function

    getInfo = Restcomm_Python_SDk.RecordingList(client).GetList()
    print(getInfo)

    #To get list of filtered Recording, call 'RecordingFilter' class and then call 'FilterCallSid' function or 'FilterPage' function
    filterlist = Restcomm_Python_SDk.RecordingFilter('1', client).FilterPage()
    print(filterlist)

def SmsExample():

    #To Send Sms, call 'SendSms' class and then call 'Send' function

    To = input("Enter the number of the receiver")
    From = input("Enter the number of the sender")
    Body = input("Enter the message")
    Sending = Restcomm_Python_SDk.SendSms(To, From, Body, client).Send()
    print(Sending)

    #To get list of all Sms, call 'SmsList' class and then call 'GetList' function

    getInfo = Restcomm_Python_SDk.SmsList(client).GetList()
    print(getInfo)

    #To filter list of Sms, call 'FilterSmsList' class and then call 'GetFilterList' function

    FilterNumber = input("Enter the Number to filter")
    filterlist = Restcomm_Python_SDk.FilterSmsList(FilterNumber, client).GetFilterlist()
    print(filterlist)

def TranscriptionExample():

    #To get list of all Transcription, call 'TranscriptionList' class and then call 'GetList' function

    getInfo = Restcomm_Python_SDk.TranscriptionList(client).GetList()
    print(getInfo)

    #To get list of filtered Transcription, call 'TranscriptionFilter' class and then call 'FilterText' function or 'FilterPage' function

    filterlist = Restcomm_Python_SDk.TranscriptionFilter('1', client).FilterPage()
    print(filterlist)

def UsageExample():

    #To get list of Usage, call 'Usage' class and then call 'GetList' function

    getInfo = Restcomm_Python_SDk.Usage(client).GetList()
    print(getInfo)

if __name__ == '__main__':
    AccountExamples()
    ApplicationExample()
    AvailableNumberExample()
    callExample()
    clientExample()
    EmailExample()
    GatewayExample()
    NotificationExample()
    RecordingExample()
    SmsExample()
    TranscriptionExample()
    UsageExample()
