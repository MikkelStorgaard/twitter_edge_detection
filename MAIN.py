import numpy
import cv2


def main():
    for path in ["image", "papeSikkandar", "sikkandarSomeguy"]:
        print("hej")
        billede = cv2.imread(f"{path}.jpg", cv2.IMREAD_COLOR)
        cv2.imshow("image", billede)
        cv2.imwrite(f"{path}raw.jpg", billede)
        cv2.waitKey(0)

        # convert img to grey
        img_grey = cv2.cvtColor(billede, cv2.COLOR_BGR2GRAY)

        filtered = cv2.bilateralFilter(img_grey, 25, 40, 40)
        cv2.imshow('image', filtered)
        cv2.imwrite(f"{path}filtered.jpg", filtered)
        cv2.waitKey(0)

        cannied = cv2.Canny(filtered, 50, 200)

        cv2.imshow('image', cannied)
        cv2.imwrite(f"{path}cannied.jpg", cannied)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
