from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.676083,8.362556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_161442.26+082145.2/sdB_SDSSJ_161442.26+082145.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_161442.26+082145.2/sdB_SDSSJ_161442.26+082145.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
