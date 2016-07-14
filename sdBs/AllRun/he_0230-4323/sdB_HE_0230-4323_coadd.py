from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[38.227792,-43.174389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_0230-4323/sdB_HE_0230-4323_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_0230-4323/sdB_HE_0230-4323_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
