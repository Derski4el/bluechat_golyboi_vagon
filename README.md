# bluechat_golyboi_vagon
chatik

Application(Web API)

"/msg/{ChatId}" POST [Auth] (token: user_id)
"/chats" POST [Auth] (token: user_id)
"/chats/{chat_id}" WS [Auth] (token: user_id) (Socket)
"/users/reg" POST
"/users/log" POST
"/users/update_token" POST
"/users/account" GET [Auth] (token: Userld)