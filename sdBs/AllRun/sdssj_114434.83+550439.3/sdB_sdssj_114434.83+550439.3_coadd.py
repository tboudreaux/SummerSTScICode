from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[176.145125,55.077583],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_114434.83+550439.3/sdB_sdssj_114434.83+550439.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_114434.83+550439.3/sdB_sdssj_114434.83+550439.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
