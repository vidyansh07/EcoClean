import { ReactNode } from 'react'

type Date_value = Date | ((date: Date) => Date)
export interface Range {
    label: ReactNode;
    value: [Date_value, Date_value];
    closeOverlay?: boolean;

    // Sets the position where the predefined range is displayed, the default is bottom.
    placement?: 'bottom' | 'left';
}
