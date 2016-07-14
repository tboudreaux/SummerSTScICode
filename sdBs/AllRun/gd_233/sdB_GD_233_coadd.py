from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[323.392042,-4.540181],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GD_233/sdB_GD_233_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GD_233/sdB_GD_233_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
