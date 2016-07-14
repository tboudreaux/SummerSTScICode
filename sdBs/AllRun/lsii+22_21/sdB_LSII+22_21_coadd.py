from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[301.239917,22.344503],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LSII+22_21/sdB_LSII+22_21_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LSII+22_21/sdB_LSII+22_21_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
