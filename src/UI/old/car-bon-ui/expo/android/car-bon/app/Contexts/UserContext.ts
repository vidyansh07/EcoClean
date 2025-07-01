import { createContext, } from 'react'
import { default_dummy_user, UserDetails } from '@/types/UserDetails'

export let Logged_In_User_Context = createContext<UserDetails>(default_dummy_user)
