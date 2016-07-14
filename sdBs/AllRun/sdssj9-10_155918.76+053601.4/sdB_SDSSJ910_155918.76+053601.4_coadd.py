from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[239.828167,5.600389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_155918.76+053601.4/sdB_SDSSJ910_155918.76+053601.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_155918.76+053601.4/sdB_SDSSJ910_155918.76+053601.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
