from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[276.183333,35.511667], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_O11_J182444+353042 /sdB_O11_J182444+353042_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
