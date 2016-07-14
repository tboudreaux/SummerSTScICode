from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[351.786542,-4.409944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_529/sdB_PHL_529_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_529/sdB_PHL_529_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
