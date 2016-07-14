from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[270.726917,38.377108],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_1801+384/sdB_fbs_1801+384_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_1801+384/sdB_fbs_1801+384_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
