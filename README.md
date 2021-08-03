# fraudulent_notification
## Task
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days, determine the number of times the client will receive a notification over all  days.

**Example**
expenditure = [10, 20, 30, 40, 50]

d = 3 

On the first three days, they just collect spending data. At day 4, trailing expenditures are [10,20,30]. The median is 20 and the day's expenditure is 40. Because 40>=2x20 , there will be a notice. The next day, trailing expenditures are [20,30,40] and the expenditures are 50 . This is less than 2x30 so no notice will be sent. Over the period, there was one notice sent.
**Note**: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two middle values.

**Function Description**

Complete the function activityNotifications in the editor below.

activityNotifications has the following parameter(s):

int expenditure[n]: daily expenditures
int d: the lookback days for median spending
Returns

int: the number of notices sent

