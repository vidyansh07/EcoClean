'use server';
import SecureLS from 'secure-ls'
import CryptoJS from 'crypto-js';


export class SecureLocalStorage {
    ls: SecureLS

    constructor(namesapce: string = "default") {
        this.ls = new SecureLS({
            encodingType: 'rabbit',
            isCompression: true,
            encryptionSecret: import.meta.env.VITE_LOCAL_STORAGE_ENCRYPTION_KEY,
            encryptionNamespace: namesapce
        });
    }


    setValueToStorage(keyname: string, data: Object) {
        try {
            this.ls.set(keyname, { items: data });
            return true
        }
        catch (e) {
            console.error("unable to set to storage : \n", e)
            return false
        }

    }

    getKeyFromStorage(keyname: string) {
        try {
            return this.ls.get(keyname)
        }
        catch (e) {
            console.error("unable to get from storage : \n", e)
            return false
        }
    }

    getAllKeysFromStorage() {
        try {
            return this.ls.getAllKeys()
        } catch (e) {
            console.error("unable to get from storage : \n", e)
            return false
        }
    }

    removeKeyFromStorage(keyname: string) {
        try {
            this.ls.remove(keyname)
            return true
        }
        catch (e) {
            console.error("unable to remvoe key from storage : \n", e)
            return false
        }
    }

}

export class SecureAuthCredentials {
    salt: any
    constructor(custom_salt: string | null = null) {
        this.salt = custom_salt ?? Math.random() * 100000
    }
    setHash(secret: string) {
        let key = CryptoJS.PBKDF2(secret, this.salt, {
            keySize: 512 / 32,
            iterations: 10000
        });
        return key.toString(CryptoJS.enc.Hex)
    }

    createDigest(credentials: object) {
        let digest = CryptoJS.HmacSHA256(JSON.stringify(credentials), import.meta.env.VITE_LOCAL_STORAGE_ENCRYPTION_KEY)
        return digest
    }
}