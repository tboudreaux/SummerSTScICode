from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[309.751708,-4.711578],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j20390-0442/sdB_galex_j20390-0442_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j20390-0442/sdB_galex_j20390-0442_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
