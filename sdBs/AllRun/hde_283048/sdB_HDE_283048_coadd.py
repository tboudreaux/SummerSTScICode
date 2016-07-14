from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[58.307125,25.756067],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HDE_283048/sdB_HDE_283048_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HDE_283048/sdB_HDE_283048_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
