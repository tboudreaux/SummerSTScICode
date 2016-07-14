from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[156.923125,34.671389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_102741.55+344017.0/sdB_sdssj_102741.55+344017.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_102741.55+344017.0/sdB_sdssj_102741.55+344017.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
