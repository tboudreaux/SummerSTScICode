from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[100.882875,14.157444], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_kpd_0640+1412/sdB_kpd_0640+1412_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
