import random
import pygame
import sys
import time
pygame.init()
to_sort = []

size = (1100,600)
window = pygame.display.set_mode(size,pygame.RESIZABLE)
background_color = (15,15,24)
pygame.display.set_caption("Quick Sort Visualized | Justin Stitt")
clock = pygame.time.Clock()
slots = []
largest = 0
global_color = (0,0,0)

class Slot():
    def __init__(self,index,value):
        self.spacing = 25 # spacing between slots
        self.multiplier = 15 # multiplier to the y value
        self.value = value
        self.index = index # where it is in to_sort
        self.pos = [self.spacing * self.index, (size[1] - (self.value * self.multiplier)) ]# x , y
        self.color = (140, 174, 241)
        self.size = [1, (size[1] - (self.value * self.multiplier)) ]
    def update(self):
        #print(self.spacing)
        self.size = [self.spacing - 1, ( (self.value * self.multiplier)) ]
        self.pos = [self.spacing * self.index, (size[1] - (self.value * self.multiplier)) ]# x , y
    def render(self):
        global global_color
        if global_color == (0,0,0):
            pygame.draw.rect(window,self.color,pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1]))
        else:
            pygame.draw.rect(window,global_color,pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1]))




def fill_list(arr,low,high,length):
    global largest
    for x in range(length):
        rand = random.randint(low,high)
        arr.append(rand)
        slots.append(Slot(x,rand))
        slots[x].spacing = (size[0] - (size[0]/75))/length
        if rand > largest:
            largest = rand
    for x in range(length):
        slots[x].multiplier = ( (size[1] - size[1]/5 )/largest)



def quick_sort(nums):
    quick_sort_helper(nums,0,len(nums)-1)

def quick_sort_helper(nums,low,high):
    if low < high:
        p = partition(nums,low,high)
        quick_sort_helper(nums,low,p - 1)
        quick_sort_helper(nums,p + 1, high)

def get_pivot(nums,low,high):
    mid = (high + low) // 2
    pivot = high
    if nums[low] < nums[mid]:
        if nums[mid] < nums[high]:
            pivot = mid
    elif nums[low] < nums[high]:
        pivot = low
    #pivot = high #Simpler
    return pivot

def partition(nums,low,high):
    global slots
    pivot_index = get_pivot(nums,low,high)
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[low] = nums[low],nums[pivot_index]
    slots[pivot_index].value , slots[low].value = slots[low].value , slots[pivot_index].value#ADDED
    border = low

    for x in range(low,high + 1):
        if nums[x] < pivot_value:
            border += 1
            nums[x],nums[border] = nums[border],nums[x]
            slots[x].value,slots[border].value = slots[border].value,slots[x].value#ADDED
    nums[low],nums[border] = nums[border],nums[low]
    slots[low].value,slots[border].value = slots[border].value,slots[low].value#ADDED


    return(border)

fill_list(to_sort,1,500,50)#THIS IS THE MAIN LIST, (list,min,max,length) (j to sort, k to do cool color stuff that is useless)

def remap(n,start1,stop1,start2,stop2):
    return ((n-start1)/(stop1-start1)) *(stop2-start2)+start2

def slide(items):
    global global_color
    for x in range(len(items) - 1):
        items[x].color = (60, 170, 211)
        items[x+1].color = (255,0,0)
        #for y in range(len(items)):
        items[x].render()
        items[x+1].render()

        pygame.display.update()
    for y in range(3):
        global_color = (130, 150, 254)
        for slot in slots:
            slot.render()
        pygame.display.update()

        time.sleep(.2)
        global_color = (140, 174, 241)
        for slot in slots:
            slot.render()
        pygame.display.update()
        time.sleep(.2)


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                quick_sort(to_sort)
                #print(to_sort)
            elif event.key == pygame.K_k:
                slide(slots)
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
    for slot in slots:
        slot.update()
def render():
    for slot in slots:
        slot.render()


while True:
    update()

    window.fill(background_color)
    render()
    pygame.display.flip()
