from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[261.900083,36.285083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_172736.02+361706.3/sdB_SDSSJ910_172736.02+361706.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_172736.02+361706.3/sdB_SDSSJ910_172736.02+361706.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
