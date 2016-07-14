from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[349.993375,-5.165497],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_feige_110/sdB_feige_110_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_feige_110/sdB_feige_110_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
