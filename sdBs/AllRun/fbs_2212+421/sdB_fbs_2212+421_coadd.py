from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[333.6485,42.3845],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2212+421/sdB_fbs_2212+421_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2212+421/sdB_fbs_2212+421_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
