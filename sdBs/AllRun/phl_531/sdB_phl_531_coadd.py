from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[351.969417,-6.231442],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_phl_531/sdB_phl_531_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_phl_531/sdB_phl_531_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
