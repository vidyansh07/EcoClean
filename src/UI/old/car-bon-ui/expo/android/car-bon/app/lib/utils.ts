import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"
import 'core-js/features/array/at'; //polyfill 

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function get_initials(
  name: string | null | undefined,
  full: boolean = false
) {
  let Name_words = name?.split(" ");
  let Name_Abbr = Name_words?.map((i) => i.toUpperCase().split("")[0]).join(
    ""
  );
  return full ? Name_Abbr : `${Name_Abbr?.at(0)}${Name_Abbr?.at(-1)}`;
};

export function title_case(str: string | undefined) {
  if (str == undefined) {
    return str
  }
  return str.replace(
    /\w\S*/g,
    (text: string) => text.charAt(0).toUpperCase() + text.substring(1).toLowerCase()
  );
}