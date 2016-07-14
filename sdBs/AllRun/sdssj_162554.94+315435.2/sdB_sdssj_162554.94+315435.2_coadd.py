from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[246.478917,31.909778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_162554.94+315435.2/sdB_sdssj_162554.94+315435.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_162554.94+315435.2/sdB_sdssj_162554.94+315435.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()